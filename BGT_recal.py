#initialise all values
A, B, C, D = [0]*5, [0]*5, [0]*5, [0]*5
#intialise ticker
t = 0

for i in range(5):
    # exclusively ask for A and B during the first iteration, i.e. t=0
    if t == 0:
        a = float(input('Enter A value: '))
        b = float(input('Enter B value: '))
        A[t] = a
        B[t] = b

    c = float(input('Enter new C value: '))
    d = float(input('Enter new D value: '))
    C[t] = c
    D[t] = d

    #Finish the code if 4 retests were conducted.
    if t == 4: 
        print("The device has been recalibrated four times, speak with supplier if all values are not within tolerance!!")
        break

    #check if A and B values are within range, if not let the user know!
    if 2 <= A[t] <= 15 and 35 <= B[t] <= 100:
        #if C and D are out of tolerance run this to calculate new A and B. 
        #if C and D are in tolerance then let the user know and end program
        if C[t] > 56 or C[t] < 50 or D[t] > 12.5 or D[t] < 10:
            print('Iteration #', t)
            if C[t]<=56 and D[t]<=12.5 and t == 0:
                A[t+1] = A[t]
                B[t+1] = 54 - C[t] + B[t]
            elif C[t]<=56 and D[t]<=12.5:
                A[t+1] = A[t]
                B[t+1] = B[t] + 4
            elif C[t]<=56 and D[t]>12.5:
                A[t+1] = A[t] - 1
                B[t+1] = B[t] + 4
            else:
                A[t+1] = A[t]
                B[t+1] = B[t] - 2
            
            t = t+1
            print('New A value is: ', A[t])
            print('New B value is: ', B[t])
            print('Now recalibrate with new A and B values!!!!')
            
        else:
            print('C and D are within tolerance, no further tests required!')
            break
    else:
        print('A or B value not within tolerance!')
        break
    #Finish program after 5 iterations
print('Program finished!!')

#######################################
import matplotlib.pyplot as plt

# Define the data for the table
data = [
    [f'A\u2080 = {A[0]}', f'A\u2081 = {A[1]}', f'A\u2082 = {A[2]}', f'A\u2083 = {A[3]}', f'A\u2084 = {A[4]}'], 
    [f'B\u2080 = {B[0]}', f'B\u2081 = {B[1]}', f'B\u2082 = {B[2]}', f'B\u2083 = {B[3]}', f'B\u2084 = {B[4]}'],
    [f'C\u2080 = {C[0]}', f'C\u2081 = {C[1]}', f'C\u2082 = {C[2]}', f'C\u2083 = {C[3]}', f'C\u2084 = {C[4]}'],
    [f'C\u2080 = {D[0]}', f'D\u2081 = {D[1]}', f'D\u2082 = {D[2]}', f'D\u2083 = {D[3]}', f'D\u2084 = {D[4]}'],

]

# Define column labels
column_labels = ['Initial run #0', 'Retry #1', 'Retry #2', 'Retry #3', 'Retry #4']

# Create a figure and a subplot
fig, ax = plt.subplots()

# Hide the plot axes
ax.axis('tight')
ax.axis('off')

# Create the table
table = ax.table(cellText=data, colLabels = column_labels, colColours = ["0.75"]*5, cellLoc='left', loc='center')

#save to png
plt.savefig('output')

# Display the table
plt.show()




