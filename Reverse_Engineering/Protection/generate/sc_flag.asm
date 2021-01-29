BITS 64;

; 64 bit print string program
; injectible shellcode
; $ nasm sc_flag.asm
; $ bin2sc.py sc_flag

Section .text

	global _start

_start:
	sub rsp, 100
		mov rcx, rsp
		mov r8,		'19C4{adv'
		mov r9,		'4nced_En'
		mov r10,	'crypt3ds'
		mov r11,	'hellCod3'
		mov r12,	'}Can u f'
		mov r13,	'ind the '
		mov r14,	'flag?   '
		mov r15,	0x0a

		push r15
		push r14
		push r13
		push r12
		push r11
		push r10
		push r9
		push r8


		mov rax, 1
		mov rdi, 1
		lea rsi, [ rcx - 31 ]	; load char ptr
		mov rdx, 58				; length
		syscall					; 64 bit uses syscall instead of int 80

		; now exit
		xor rbx, rbx
		mov rax, 60			; 60 is sys_exit in x64 
		syscall


