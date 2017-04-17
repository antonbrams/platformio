


# How to Platformio

###### Prepare
- install platformio with `brew install platformio`
- show boards for arduino `pio boards arduino`

###### ISP
- do in `./isp` the `pio run` to upload the ISP Programmer to the `Arduino Nano`
- burn the Bootloader in `./boot` with `pio run -e 85 -t burn` to the `ATTIny85` Board

###### Compiling
- compile in `./blink` the `pio run -e nano`
- clear `pio run -t clear`

###### Serial
- show serial devices `pio device list`
- to monitor `pio device monitor` or `pio device monitor -p /dev/cu.wchusbserial14110 -b 9600`
- stop `Ctrl+]`


