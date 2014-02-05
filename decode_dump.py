#!/usr/bin/env python

import binascii
import re
import sys

def main(args):
	# in kilobytes
	DUMP_SIZE = int(args[1]) if len(args) > 1 else False

	HEADER = "DumpPebble.c"
	BYTES_WRITTEN = 0
	LAST_ADDR = -1
	BLOCK_SIZE = 32

	regex = re.compile("%s.+0x([0-9a-fA-F]+): ([0-9a-fA-F]+)" % HEADER)

	with open(args[0]) as f:
		with open(args[0]+".bin", "wb") as fw:
			for line in f.readlines():
				parts = regex.findall(line)
				if len(parts) == 0:
					continue

				addr = int(parts[0][0], 16)
				bytes = binascii.unhexlify(parts[0][1])

				if LAST_ADDR == -1 or (LAST_ADDR + BLOCK_SIZE) == addr:
					LAST_ADDR = addr
				else:
					raise Exception("Bad step (%d) at: %s " % ((addr-LAST_ADDR), line))

				BYTES_WRITTEN += len(bytes)
				fw.write(bytes)

	if DUMP_SIZE:
		TOTAL = DUMP_SIZE * 1024
		PERCENT = (float(BYTES_WRITTEN) / float(TOTAL)) * 100

		print "Dumped %d bytes of %d (%2.2f%%)" % (BYTES_WRITTEN, TOTAL, PERCENT)
	else:
		print "Dumped %d bytes" % (BYTES_WRITTEN)


if __name__ == "__main__":
    main(sys.argv[1:])