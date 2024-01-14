section .data
    mensagem db 'Bem vindo ao OIA - Otavio Inteligence Artificial$', 0 
    ; mensagem assembly

section .text
    global _start

_start:
    
    mov ah, 09h         
    mov dx, mensagem    
    int 21h             
    mov ah, 4Ch         
    int 21h             
