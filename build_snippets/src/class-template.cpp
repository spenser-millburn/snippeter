class ClassName {
private:
    // Private members
    int data;

public:
    // Constructor
    ClassName() : data(0) {}

    // Parameterized constructor
    ClassName(int val) : data(val) {}

    // Destructor
    ~ClassName() {}

    // Getter
    int getData() const {
        return data;
    }

    // Setter
    void setData(int val) {
        data = val;
    }

    // Member function
    void display() const {
        std::cout << "Data: " << data << std::endl;
    }
};