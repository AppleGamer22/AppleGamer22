# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 21
## What is the value of `local_ch` when its corresponding `movl` instruction is called (first if multiple)?
```bash
$ r2 -d challenge1
[0x00400a30]> e asm.syntax=intel
[0x00400a30]> aaaa
[0x00400a30]> afl | grep "main"
0x00400de0  114 1657         sym.__libc_start_main
0x0048fa40   16 247  -> 237  sym._nl_unload_domain
0x00403ae0  308 5366 -> 5301 sym._nl_load_domain
0x00470430    1 49           sym._IO_switch_to_main_wget_area
0x00403840   39 672  -> 640  sym._nl_find_domain
0x00400b4d    1 35           main
0x0048f9f0    7 73   -> 69   sym._nl_finddomain_subfreeres
0x0044ce10    1 8            sym._dl_get_dl_main_map
0x00415ef0    1 43           sym._IO_switch_to_main_get_area
[0x00400a30]> pdf @main
            ; DATA XREF from entry0 @ 0x400a4d
┌ 35: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_ch @ rbp-0xc
│           ; var int64_t var_8h @ rbp-0x8
│           ; var int64_t var_4h @ rbp-0x4
│           0x00400b4d      55             push rbp
│           0x00400b4e      4889e5         mov rbp, rsp
│           0x00400b51      c745f4010000.  mov dword [var_ch], 1
│           0x00400b58      c745f8060000.  mov dword [var_8h], 6
│           0x00400b5f      8b45f4         mov eax, dword [var_ch]
│           0x00400b62      0faf45f8       imul eax, dword [var_8h]
│           0x00400b66      8945fc         mov dword [var_4h], eax
│           0x00400b69      b800000000     mov eax, 0
│           0x00400b6e      5d             pop rbp
└           0x00400b6f      c3             ret
[0x00400a30]> db 0x00400b51
[0x00400a30]> db 0x00400b62
[0x00400a30]> db 0x00400b69
[0x00400a30]> dc
hit breakpoint at: 0x400b51
[0x00400b51]> pdf @main
            ; DATA XREF from entry0 @ 0x400a4d
            ;-- rax:
┌ 35: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_ch @ rbp-0xc
│           ; var int64_t var_8h @ rbp-0x8
│           ; var int64_t var_4h @ rbp-0x4
│           0x00400b4d      55             push rbp
│           0x00400b4e      4889e5         mov rbp, rsp
│           ;-- rip:
│           0x00400b51 b    c745f4010000.  mov dword [var_ch], 1
│           0x00400b58      c745f8060000.  mov dword [var_8h], 6
│           0x00400b5f      8b45f4         mov eax, dword [var_ch]
│           0x00400b62 b    0faf45f8       imul eax, dword [var_8h]
│           0x00400b66      8945fc         mov dword [var_4h], eax
│           0x00400b69 b    b800000000     mov eax, 0
│           0x00400b6e      5d             pop rbp
└           0x00400b6f      c3             ret
[0x00400b51]> px @rbp-0xc
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffffde498e4  0000 0000 1890 6b00 0000 0000 4018 4000  ......k.....@.@.
0x7ffffde498f4  0000 0000 e910 4000 0000 0000 0000 0000  ......@.........
0x7ffffde49904  0000 0000 0000 0000 0100 0000 189a e4fd  ................
0x7ffffde49914  ff7f 0000 4d0b 4000 0000 0000 0000 0000  ....M.@.........
0x7ffffde49924  0000 0000 1700 0000 7100 0000 0000 0000  ........q.......
0x7ffffde49934  0000 0000 7000 0000 0000 0000 0000 0000  ....p...........
0x7ffffde49944  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffffde49954  0000 0000 0000 0000 0000 0000 0004 4000  ..............@.
0x7ffffde49964  0000 0000 e239 a3aa a181 6a6d e018 4000  .....9....jm..@.
0x7ffffde49974  0000 0000 0000 0000 0000 0000 1890 6b00  ..............k.
0x7ffffde49984  0000 0000 0000 0000 0000 0000 e239 23a8  .............9#.
0x7ffffde49994  e87a 9592 e239 17bb a181 6a6d 0000 0000  .z...9....jm....
0x7ffffde499a4  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffffde499b4  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffffde499c4  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffffde499d4  0000 0000 0000 0000 0000 0000 0000 0000  ................
[0x00400b51]> ds
hit breakpoint at: 0x400b62
[0x00400b62]> px @rbp-0xc
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fff3617e294  0100 0000 0600 0000 0000 0000 4018 4000  ............@.@.
0x7fff3617e2a4  0000 0000 e910 4000 0000 0000 0000 0000  ......@.........
0x7fff3617e2b4  0000 0000 0000 0000 0100 0000 c8e3 1736  ...............6
0x7fff3617e2c4  ff7f 0000 4d0b 4000 0000 0000 0000 0000  ....M.@.........
0x7fff3617e2d4  0000 0000 1700 0000 7100 0000 0000 0000  ........q.......
0x7fff3617e2e4  0000 0000 7000 0000 0000 0000 0000 0000  ....p...........
0x7fff3617e2f4  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fff3617e304  0000 0000 0000 0000 0000 0000 0004 4000  ..............@.
0x7fff3617e314  0000 0000 bcb6 85d3 497a 0383 e018 4000  ........Iz....@.
0x7fff3617e324  0000 0000 0000 0000 0000 0000 1890 6b00  ..............k.
0x7fff3617e334  0000 0000 0000 0000 0000 0000 bcb6 6526  ..............e&
0x7fff3617e344  e616 fd7c bcb6 31c2 497a 0383 0000 0000  ...|..1.Iz......
0x7fff3617e354  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fff3617e364  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fff3617e374  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7fff3617e384  0000 0000 0000 0000 0000 0000 0000 0000  ................
[0x00400b51]> dc
hit breakpoint at: 0x400b62
[0x00400b62]> ds
[0x00400b62]> dr
rax = 0x00000006
rbx = 0x00400400
rcx = 0x0044b9a0
rdx = 0x7ffe09b4af48
r8 = 0x00040000
r9 = 0x006bb8e0
r10 = 0x00000015
r11 = 0x00000000
r12 = 0x004018e0
r13 = 0x00000000
r14 = 0x006b9018
r15 = 0x00000000
rsi = 0x7ffe09b4af38
rdi = 0x00000001
rsp = 0x7ffe09b4ae10
rbp = 0x7ffe09b4ae10
rip = 0x00400b66
rflags = 0x00000246
orax = 0xffffffffffffffff
0x00400b62]> dc
hit breakpoint at: 0x400b69
[0x00400b69]> pdf @main
            ; DATA XREF from entry0 @ 0x400a4d
┌ 35: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_ch @ rbp-0xc
│           ; var int64_t var_8h @ rbp-0x8
│           ; var int64_t var_4h @ rbp-0x4
│           0x00400b4d      55             push rbp
│           0x00400b4e      4889e5         mov rbp, rsp
│           0x00400b51 b    c745f4010000.  mov dword [var_ch], 1
│           0x00400b58      c745f8060000.  mov dword [var_8h], 6
│           0x00400b5f      8b45f4         mov eax, dword [var_ch]
│           0x00400b62 b    0faf45f8       imul eax, dword [var_8h]
│           0x00400b66      8945fc         mov dword [var_4h], eax
│           ;-- rip:
│           0x00400b69 b    b800000000     mov eax, 0
│           0x00400b6e      5d             pop rbp
└           0x00400b6f      c3             ret
[0x00400b69]> px @rbp-0x4
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffe09b4ae0c  0600 0000 4018 4000 0000 0000 e910 4000  ....@.@.......@.
0x7ffe09b4ae1c  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffe09b4ae2c  0100 0000 38af b409 fe7f 0000 4d0b 4000  ....8.......M.@.
0x7ffe09b4ae3c  0000 0000 0000 0000 0000 0000 1700 0000  ................
0x7ffe09b4ae4c  7100 0000 0000 0000 0000 0000 7000 0000  q...........p...
0x7ffe09b4ae5c  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffe09b4ae6c  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffe09b4ae7c  0000 0000 0004 4000 0000 0000 2f1a 73ce  ......@...../.s.
0x7ffe09b4ae8c  a2cb 258c e018 4000 0000 0000 0000 0000  ..%...@.........
0x7ffe09b4ae9c  0000 0000 1890 6b00 0000 0000 0000 0000  ......k.........
0x7ffe09b4aeac  0000 0000 2f1a b3a2 4bd8 d973 2f1a c7df  ..../...K..s/...
0x7ffe09b4aebc  a2cb 258c 0000 0000 0000 0000 0000 0000  ..%.............
0x7ffe09b4aecc  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffe09b4aedc  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffe09b4aeec  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffe09b4aefc  0000 0000 0000 0000 0000 0000 0000 0000  ................
```
## What is the value of `eax` when the `imull` instruction is called?

## What is the value of `local_4h` before eax is set to 0?

