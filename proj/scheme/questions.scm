(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
  (define (helper pairs so-far)
    (cond 
      ((eqv? pairs nil) so-far)
      (else (helper (cdr pairs) 
        (list (append (car so-far) (list (caar pairs))) (append (cadr so-far) (map let-to-lambda (cdar pairs))))))
    )
  )
  (helper pairs '(() ()))
)


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (helper s idx so-far)
    (cond 
      ((eqv? s nil) so-far)
      (else (helper (cdr s) (+ idx 1) (append so-far (list (list idx (car s))))))
    )
  )
  (helper s 0 '())
)
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (define (helper list1 list2 so-far)
    (cond 
      ((eqv? list1 nil) (append so-far list2))
      ((eqv? list2 nil) (append so-far list1))
      ((comp (car list1) (car list2)) (helper (cdr list1) list2 (append so-far (list (car list1)))))
      (else (helper (cdr list2) list1 (append so-far (list (car list2)))))
    )
  )
  (helper list1 list2 '())
)
  ; END PROBLEM 16


;; Problem 17

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 17
         expr
         ; END PROBLEM 17
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 17
         (list 'quote (cadr expr))
         ; END PROBLEM 17
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
            (append (list 'lambda params) (map let-to-lambda body))
           ; END PROBLEM 17
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           (append (list (append (list 'lambda (car (zip values))) (map let-to-lambda body))) (cadr (zip values)))
           ; END PROBLEM 17
           ))
        (else
         ; BEGIN PROBLEM 17
         (let
          ((operator (car expr))
           (operands (cdr expr)))
          (append (list (let-to-lambda operator)) (map let-to-lambda operands))
         )
         ; END PROBLEM 17
         )))