


Import("env")

env.Replace(
	SETFUSECMD='$UPLOADER $UPLOADERFLAGS -Ulock:w:0xFF:m -Uefuse:w:0xFF:m -Uhfuse:w:0xD7:m -Ulfuse:w:0xE2:m',
	UPLOADBOOTCMD='$UPLOADER $UPLOADERFLAGS -Uflash:w:$SOURCES:i -Ulock:w:0xFF:m')

# copied from ${HOME}/Library/Arduino15/packages/ATTinyCore/hardware/avr/1.1.2/bootloaders/empty/empty_all.hex
AlwaysBuild(env.Alias(
	"burn", "./empty_all.hex", [
	env.VerboseAction(env.AutodetectUploadPort, "Looking for upload port..."),
	env.VerboseAction("$SETFUSECMD", "Setting fuses"),
	env.VerboseAction("$UPLOADBOOTCMD", "Uploading bootloader $SOURCE")]))


