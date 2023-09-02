(define (split-at lst n)
    (cond 
        ((> n (length lst)) (list lst))
        ((= n 0) (cons nil lst))
        (else (let ((x (split-at lst (- n 1))))
                (cons (append (car x) (list (car (cdr x)))) (cdr (cdr x)))
            )
        )
    )
)

(define (compose-all funcs)
    (cond 
        ((eqv? funcs nil) (lambda (x) x))
        (else (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
    )
)
