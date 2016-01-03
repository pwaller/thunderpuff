import dis
import sys


def caller_assignment_name(depth=0):
    frame = sys._getframe(depth + 2)

    dis.disassemble(frame.f_code, frame.f_lasti)

    # from pprint import pprint
    # pprint(list(dis.get_instructions(frame.f_code)))

    for op in list(dis.get_instructions(frame.f_code)):
        if op.offset < frame.f_lasti:
            continue
        if op.starts_line is not None:
            # We hit a new source line.
            break
        if op.opname == "STORE_NAME":
            return op.argval

    raise RuntimeError("Return value of caller must be assigned to a variable")
