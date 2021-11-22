from gradelib import *

r = Runner(save("jos.out"),
           stop_breakpoint("readline"))

@test(30, "sys_ept_tests")
def sys_ept_map_test():
    r.run_qemu()
    r.match("Cheers! sys_ept_map seems to work correctly")

def matchtest(parent, name, points, *args, **kw):
    def do_test():
        r.match(*args, **kw)
    test(points, name, parent=parent)(do_test)

@test(0, "VMM Tests")
def test_vm():
    r.user_test("vmm")
matchtest(test_vm,"start vmxon:", 10, "VMXON")

matchtest(test_vm, "VMX extension test:", 20, "VMX extension hidden from guest")

matchtest(test_vm, "Print message in VM:", 30, "What is the tortoise")

matchtest(test_vm, "VM correctly started:", 10, "vm\$")

run_tests()
