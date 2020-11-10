	.file	"B2.c"
	.text
	.comm	_N, 4, 2
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB13:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$10, 8(%esp)
	movl	$0, 12(%esp)
	jmp	L2
L3:
	movl	_N, %eax
	addl	%eax, 8(%esp)
	addl	$1, 12(%esp)
L2:
	cmpl	$3, 12(%esp)
	jle	L3
	movl	8(%esp), %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE13:
	.ident	"GCC: (MinGW.org GCC Build-2) 9.2.0"
