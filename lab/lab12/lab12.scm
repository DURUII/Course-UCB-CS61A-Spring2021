(define (tail-replicate x n)
  (define (helper n so-far)
    (cond 
      ((= n 0) so-far)
      (else (helper (- n 1) (cons x so-far)))
    )
  )

  (helper n '())
)

(define-macro (def func args body)
  `(define (,func ,@args) ,body)
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y)
      )
  )
)
