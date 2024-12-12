# QA Automation Assignment: Web Calculator


## **Test Scenarios**

### **1. Positive Tests**
- **Addition**: Verifies that the calculator correctly adds two numbers.
- **Subtraction**: Verifies that the calculator correctly subtracts two numbers.
- **Multiplication**: Verifies that the calculator correctly multiplies two numbers.
- **Division**: Verifies that the calculator correctly divides two numbers.
- **Decimal Support**: Verifies that decimal numbers are correctly handled.

### **2. Negative Tests**
- **Invalid Input**: Verifies the calculator displays an error when non-numeric input is entered.
- **Division by Zero**: Verifies the calculator displays an error for division by zero.
- **Empty Input**: Verifies the calculator handles empty fields correctly.

### **3. Edge Cases**
- **Large Numbers**: Verifies calculations involving large numbers.
- **Negative Numbers**: Verifies calculations with negative numbers.
- **Addition with Zero**: Verifies that adding zero to a number works as expected.

---
## **Things I couldn't test**
- Boundary values - no maximum or minimum numbers were mentioned
- Error handling - no errors mentioned, I assumed there are generic errors for the written problems like divison by zero


## **Setup Instructions**

### **1. Prerequisites**
- Install Python 3.7 or later.
- Install Google Chrome or a compatible browser.
- Install ChromeDriver (or the appropriate WebDriver for your browser).

### **2. Install Dependencies**
Install the required Python libraries using `pip`:
```bash
pip install -r requirements.txt
```
---

## **How to Run the Tests**

Run the following command to execute the test suite:
```bash
pytest test_calculator.py
```

### **Generate HTML Report**
To generate a detailed HTML report of the test results:
```bash
pytest test_calculator.py --html=report.html --self-contained-html
```


