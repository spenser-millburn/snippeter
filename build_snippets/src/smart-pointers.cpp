#include <memory>
#include <iostream>
#include <vector>

class MyClass {
public:
    MyClass(int val) : value(val) {
        std::cout << "Constructor: " << value << std::endl;
    }
    ~MyClass() {
        std::cout << "Destructor: " << value << std::endl;
    }
    void display() {
        std::cout << "Value: " << value << std::endl;
    }
private:
    int value;
};

int main() {
    // unique_ptr - exclusive ownership
    std::unique_ptr<MyClass> ptr1 = std::make_unique<MyClass>(10);
    ptr1->display();

    // Transfer ownership
    std::unique_ptr<MyClass> ptr2 = std::move(ptr1);
    // ptr1 is now nullptr

    // shared_ptr - shared ownership
    std::shared_ptr<MyClass> sptr1 = std::make_shared<MyClass>(20);
    {
        std::shared_ptr<MyClass> sptr2 = sptr1; // Reference count = 2
        sptr2->display();
        std::cout << "Use count: " << sptr1.use_count() << std::endl;
    } // sptr2 destroyed, reference count = 1

    std::cout << "Use count: " << sptr1.use_count() << std::endl;

    // weak_ptr - non-owning reference
    std::weak_ptr<MyClass> wptr = sptr1;
    if (auto locked = wptr.lock()) {
        locked->display();
    }

    // Vector of unique_ptrs
    std::vector<std::unique_ptr<MyClass>> vec;
    vec.push_back(std::make_unique<MyClass>(30));
    vec.push_back(std::make_unique<MyClass>(40));

    return 0;
}