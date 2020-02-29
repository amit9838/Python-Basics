#include<iostream>
int main(int argc, char const *argv[])
{
	/* code */
	return 0;
}
{
	int exper, age, salary;
	cout << "The person  is experienced? "
	     << "Enter 1 for yes, 0 for no.: "
	cin >> exper;
	cout << "\n Enter age of the person: ";
	cin >> age;
	salary = (exper)?((age>35)?6000:(age>28)?4800:3000):2000;
	cout << "\n The salary of the person is "<< salary<<"\n";
	return 0;
}