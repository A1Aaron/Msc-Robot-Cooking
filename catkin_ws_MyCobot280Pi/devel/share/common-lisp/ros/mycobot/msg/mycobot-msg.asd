
(cl:in-package :asdf)

(defsystem "mycobot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "joint" :depends-on ("_package_joint"))
    (:file "_package_joint" :depends-on ("_package"))
  ))