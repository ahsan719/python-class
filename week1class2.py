name="Ahsan"
cgpa=2.9
attendance=85
income=115000

if cgpa>=3.5 and attendance>=80:

    if income<100000:
        print("Full scholarship")
    else:
        print("Merit Scholrship") 


elif cgpa>3.0:
    print("partial Schoalrship")

else:
    print("not eligible")  