f = open('dir/other_dir/bin_data', 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()