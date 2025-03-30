"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Ashrit Perepu and <FULL NAME>, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ap59673
UT EID 2:
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        x = Node(exp, coeff)
        if self.head.exp or self.head < exp:
            i = self.head
            while i.next.exp and i.next >= exp:
                i = i.next
            x.next = i.next
            i.next = x
        elif self.head.exp and self.head >= exp:
            x.next = self.head
            self.head = x   
        pass

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        f = self.head
        n = p.head
        a = LinkedList()
        while f or n:
            if f and n and f.exp == n.exp:
                s = f.coeff + n.coeff
                if s:
                    a.insert(s, f.exp)
                f = f.next
                n = n.next
            elif f and (not n or f.exp > n.exp):
                a.insert(f.coeff, f.exp)
                f = f.next
            elif n and (not f or n.exp > f.exp):
                n = n.next
        return a                    

        pass

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        f = self.head
        a = LinkedList()
        while f:
            t = LinkedList()
            n = p.head
            while n:
                t.insert(f.coeff * n.coeff, f.exp + n.exp)
                n = n.next
            a = a.add(t)
            f = f.next 
        return a       

        pass

    # Return a string representation of the polynomial.
    def __str__(self):
        h = self.head
        l = []
        while h:
            l.append(f"{h.coeff} {h.exp}")
            h = h.next
        return " 0 ".join(l) if not h else " -> "    
        pass


def main():
    # read data from stdin (terminal/file) using input() and create polynomial p

    # read data from stdin (terminal/file) using input() and create polynomial q

    # get sum of p and q as a new linked list and print sum

    # get product of p and q as a new linked list and print product
    y = open('input.txt', 'r')
    p = int(input())
    for i in range(p):
        q = LinkedList
        q_2 = LinkedList()
        j = int(input())
        for i in range(j):
            coeff, exp = input().split()
            j.insert(int(coeff), int(exp))
        z = int(input())
        for i in range(z):
            coeff, exp = input().split()
            z.insert(int(coeff), int(exp))
        c = j.add(z)
        c_h = j.multiply(z)         
        print(c)
        print(c_h)
    pass


if __name__ == "__main__":
    main()
