(define-macro (switch expr cases)
	(cons 'cond
		(map 
      (lambda (case) 
        (cons (equal? (eval expr) (car case)) (cdr case))
      )
    	cases
    )
  )
)