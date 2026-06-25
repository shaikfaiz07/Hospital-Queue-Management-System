class Patient:
    def __init__(self, name, age, token, priority):
        self.name = name
        self.age  = age
        self.token = token
        self.priority = priority


class HospitalQueue:

    def __init__(self):
        self.queue = []

    def insert(self):

        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        token = int(input("Enter Token Number: "))

        print("\nPriority Levels")
        print("1 - Emergency")
        print("2 - Visiting")
        print("3 - Regular Checkup")
        print("4 - Medicine")

        priority = int(input("Enter Priority: "))

        patient = Patient(name,age, token, priority)

        self.queue.append(patient)

        self.queue.sort(key=lambda x: x.priority)

        print("\nPatient Added Successfully!")

    def delete(self):

        if not self.queue:
            print("\nNo More Patients")
            return

        patient = self.queue.pop(0)

        print(f"\nPatient Treated: {patient.name}")
        print(f"Token Number: {patient.token}")

    def display(self):

        if not self.queue:
            print("\nQueue is Empty")
            return

        print("\n--------------------------------")
        print("Priority\tName\tAge\tToken")
        print("--------------------------------")

        for patient in self.queue:
            print(patient.priority,
                patient.name,
                patient.age,
                patient.token)


hospital = HospitalQueue()

while True:

    print("\n===== HOSPITAL QUEUE MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Treat Patient")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        hospital.insert()

    elif choice == 2:
        hospital.delete()

    elif choice == 3:
        hospital.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")