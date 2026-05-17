#!/usr/bin/env python3
import re

# Read the INPUT file to get expected token counts from \gla
input_path = r'C:\Users\trinley\Obsidian\abhidhamma-rails\retry-batches\retry-14.txt'

try:
    with open(input_path, 'r', encoding='utf-8') as f:
        in_text = f.read()
except:
    print(f"Could not read input file: {input_path}")
    exit(1)

# Parse expected tokens from input
expected = {}
for chunk in re.split(r'^@@', in_text, flags=re.M):
    if not chunk.strip():
        continue
    lines = chunk.strip().split('\n')
    m = re.match(r'^(\S+)\s+\(EXPECTED_TOKENS=(\d+)\)', lines[0])
    if m:
        bid = m.group(1)
        if not bid.startswith('^'):
            bid = '^' + bid
        n_expected = int(m.group(2))

        # Find the \gla line and count tokens
        gla_line = None
        for ln in lines[1:]:
            if ln.startswith('\\gla '):
                gla_line = ln.split(None, 1)[1] if len(ln.split(None, 1)) > 1 else ''
                break

        if gla_line:
            # Count tokens in gla (space-separated)
            gla_tokens = gla_line.split()
            n_actual = len(gla_tokens)
            expected[bid] = (n_expected, n_actual)
            if n_actual != n_expected:
                print(f"WARNING: {bid} - expected {n_expected} but \\gla has {n_actual} tokens")
            else:
                print(f"OK: {bid} - {n_actual} tokens")

# Read the OUTPUT file
output_path = r'C:\Users\trinley\Obsidian\abhidhamma-rails\outputs\retry-14.txt'

try:
    with open(output_path, 'r', encoding='utf-8') as f:
        out_text = f.read()
except:
    print(f"Could not read output file: {output_path}")
    exit(1)

# Parse output blocks and count tokens in glb and glc
out_blocks = {}
for chunk in re.split(r'^@@', out_text, flags=re.M):
    if not chunk.strip():
        continue
    lines = chunk.strip().split('\n')
    bid = lines[0].strip().split()[0]
    if not bid.startswith('^'):
        bid = '^' + bid

    glb = None
    glc = None
    for ln in lines[1:]:
        if ln.startswith('\\glb '):
            glb_text = ln.split(None, 1)[1] if len(ln.split(None, 1)) > 1 else ''
            glb = len(glb_text.split())
        elif ln.startswith('\\glc '):
            glc_text = ln.split(None, 1)[1] if len(ln.split(None, 1)) > 1 else ''
            glc = len(glc_text.split())

    out_blocks[bid] = (glb, glc)

# Verify
print(f"\n{'='*70}")
print("VERIFICATION RESULTS")
print(f"{'='*70}")

fails = []
for bid, (n_expected, n_actual_gla) in sorted(expected.items()):
    if bid not in out_blocks:
        print(f"FAIL: {bid} - missing from output")
        fails.append((bid, n_expected, None, None))
        continue

    glb_count, glc_count = out_blocks[bid]

    if glb_count is None or glc_count is None:
        print(f"FAIL: {bid} - missing \\glb or \\glc line")
        fails.append((bid, n_expected, glb_count, glc_count))
        continue

    if glb_count != n_expected or glc_count != n_expected:
        print(f"FAIL: {bid} - expected {n_expected} tokens, got glb={glb_count} glc={glc_count}")
        fails.append((bid, n_expected, glb_count, glc_count))
    else:
        print(f"PASS: {bid} - {n_expected} tokens")

print(f"\n{'='*70}")
print(f"BLOCKS_PROCESSED: {len(expected)}")
print(f"BLOCKS_PASSING_VERIFICATION: {len(expected) - len(fails)}")
print(f"BLOCKS_FAILED: {len(fails)}")
if fails:
    print(f"FAILED_IDS: {[f[0] for f in fails]}")
else:
    print(f"FAILED_IDS: none")
