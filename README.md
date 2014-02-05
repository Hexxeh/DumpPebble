DumpPebble
==========

Notes
-----

This is awful, but it works. Mostly...

MPU will kill your app if you start poking regions of memory it doesn't want you to. Install a firmware where the MPU is disabled to avoid this.

Usage
-----

 - Edit the memory ranges DUMP_{START,END} in DumpPebble.c
 - pebble.py build
 - pebble.py install
 - Restart your Pebble (hold back, up and enter)
 - pebble.py logs &> dump.txt
 - Now launch the app on your watch

Now in another shell...

 - decode_dump.py dump.txt (feel free to add a third arg which is the requested dump size in KB to get completed percentage)
 - Default offsets dump all of the internal flash
 - Expect it to take 20-30 minutes
 - Once it's done, your region will be dumped as dump.txt.bin
