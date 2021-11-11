import random
from random import randrange   #นำมาแรนดอมค่า int
import copy
from terminaltables import AsciiTable

#create varible
population = 10              #จำนวนบุคลากรที่ต้องการ
ga = 2                       #จำนวนกะ 2 คือ เช้า ดึก
ga_per_day = 1               #จำนวนกะต่อ 1 วัน
pop_per_ga = 2               #จำนวนคนต่อ 1 กะ
day = 7                      #จำนวนกะทั้งหมด
array_ga = []                #อาร์เรย์กะ (กะว่าไม่อยากจะทำเลย)
ga_more5day = []             #คนที่ทำงานเกิน 5 วัน/1สัปดาห์
gaStop_more2day = []         #หยุดติดกันมากกว่า 2 วัน
gamore_inOneDay = []         #1วันทำงานได้แค่ 1 กะ
near_ga = []                 #ทำงานกะติดกัน
moreNameInOneGa =[]          #1กะมีได้แค่ 1 ชื่อเท่านั้น
fitnessError = 0             #ค่า fitness

array_gaBest = []            #อาร์เรย์กะที่ดีที่สุด BEST
ga_more5dayBest = []         #คนที่ทำงานเกิน 5 วัน/1สัปดาห์ BEST
gaStop_more2dayBest = []     #หยุดติดกันมากกว่า 2 วัน BEST
gamore_inOneDayBest = []     #1วันทำงานได้แค่ 1 กะ BEST
near_gaBest = []             #ทำงานกะติดกัน BEST
moreNameInOneGaBest =[]      #1กะมีได้แค่ 1 ชื่อเท่านั้น BEST
fitnessErrorBest = 0         #ค่า fitness ที่ดีที่สุด BEST

# find fitness error หาค่า error ที่น้อยที่สุด ################################################################################
def findFitnessError(array_ga_input):
    array_ga = array_ga_input
    fitness_Error = 100                   #กำหนดค่าคะแนนเริ่มต้นเท่ากับ 100
    minusPoint_nearga = 10                #หักคะแนนเมื่อมีคนทำงานกะติดกัน เช่น ดึกไปเช้า
    minusPoint_more5day = 5               #หักคะแนนเมื่อมีคนทำงานมากกว่า 5 กะ
    minusPoint_0more2day = 5              #หักคะแนนเมื่อมีคนหยุดติดต่อกันมากกว่า 2 วัน
    minusPoint_gaMoreInOneDay = 10        #หักคะแนนเมื่อมีคนทำงานใน 1 วัน มากกว่า 1 กะ
    minusPoint_moreNameInOneGa = 10       #หักคะแนนเมื่อมีชื่อเกินใน 1 กะ
    find_nearga = []                      #หาว่าใครทำงานกะติดกัน เช่น ดึกไปเช้า
    find_ga_more5day = []                 #หาว่ามีใครที่ทำงานเกิน 5 กะต่อ 1 สัปดาห์หรือไม่
    find_gaStop_more2day = []             #หาว่ามีใครหยุดทำงานเกินติดต่อกันมากกว่า 2 กะหรือไม่
    find_gamore_inOneDay = []             #หาว่ามีใครทำงานเกินมากกว่า 2 กะใน 1 วันหรือไม่
    find_moreNameInOneGa = []             #1กะมีได้แค่ 1 ชื่อเท่านั้น

    for i in range(population):
        sum5 = 0
        sumMornMid = 0
        # 1.ตรวจหาว่าทำงานกะติดกันหรือไม่ #########################################################
        for j in range((day*2)-1):
            if(pop_per_ga > len(list(set(array_ga[j]) - set(array_ga[j+1])))):
                for k in range(pop_per_ga):
                    for l in range(pop_per_ga):
                        if(array_ga[j][k]==array_ga[j+1][l] and i==array_ga[j][k]):
                            sumMornMid = sumMornMid + 1
        # 1.ตรวจเช็คว่าทำงานกะติดกันหรือไม่
        if (sumMornMid > 0):
            find_nearga.append(i)
            fitness_Error = fitness_Error - (minusPoint_nearga * sumMornMid)
        ###################################################################################
        # 5.ตรวจหาว่ามีชื่อในกะเดียวกันซ้ำติดกันหรือไม่ #################################################
        sumMoreName1 = 0
        for j in range((day*2)-1):
            sumMoreName = 0
            for k in range(pop_per_ga):
                if (i == array_ga[j][k]):
                    sumMoreName = sumMoreName + 1
            if(sumMoreName>1):
                sumMoreName1 = sumMoreName1 + 1
        if(sumMoreName1>0):
            find_moreNameInOneGa.append(i)
            fitness_Error = fitness_Error - (minusPoint_moreNameInOneGa*sumMoreName1)
        ###################################################################################
        for j in range(day):
            sum0more2 = 0
            sum1ga = 0
            for k in range(pop_per_ga):
                # 2.ตรวจหาเกิน 5 กะ
                if(i==array_ga[j*2][k] or i==array_ga[(j*2)+1][k]):
                    sum5 = sum5 + 1
                # 3.ตรวจหาหยุดติดต่อกัน 3
                if (j + 2 < day):
                    if (i != array_ga[j*2][k] and i != array_ga[(j*2)+1][k]):
                        # print("1=",j*2,k,"2=",(j*2) + 1,k)
                        sum0more2 = sum0more2 + 1
                    if (i != array_ga[(j*2)+2][k] and i != array_ga[(j*2)+3][k]):
                        # print("3=",(j*2)+2,k,"4=",(j*2) + 1,k)
                        sum0more2 = sum0more2 + 1
                    if (i != array_ga[(j*2)+4][k] and i != array_ga[(j*2)+5][k]):
                        # print("5=",(j*2)+4,k,"6=",(j*2) + 5,k)
                        sum0more2 = sum0more2 + 1
                # 4.ตรวจหาทำงานใน 1 วัน มากกว่า 1 กะ
                if (i == array_ga[j*2][k]):
                    sum1ga = sum1ga + 1
                if (i == array_ga[(j*2)+1][k]):
                    sum1ga = sum1ga + 1
            # 4.ตรวจเช็คทำงานใน 1 วัน มากกว่า 1 กะ
            if (sum1ga > 1):
                check_inOneDay_inArray = False
                for l in range(len(find_gamore_inOneDay)):
                    if(i==find_gamore_inOneDay[l]):
                        check_inOneDay_inArray = True
                        break
                if(check_inOneDay_inArray==False):
                    find_gamore_inOneDay.append(i)
                    fitness_Error = fitness_Error - (minusPoint_gaMoreInOneDay*sum1ga)
            # 3.ตรวจเช็คหยุดติดต่อกัน 3
            if (sum0more2 == pop_per_ga * 3):  # 3คือ3วันติดกัน
                check_more2day_inArray = False
                for l in range(len(find_gaStop_more2day)):
                    if(i==find_gaStop_more2day[l]):
                        check_more2day_inArray = True
                        break
                if(check_more2day_inArray == False):
                    find_gaStop_more2day.append(i)
                    fitness_Error = fitness_Error - minusPoint_0more2day
        # 2.ตรวจเช็คเกิน 5 กะ
        if(sum5>5):
            find_ga_more5day.append(i)
            fitness_Error = fitness_Error - minusPoint_more5day

    return find_ga_more5day,find_gaStop_more2day,find_gamore_inOneDay,find_nearga,find_moreNameInOneGa,fitness_Error

########################################################################################################################
# แบบ random ###########################################################################################################
def randomMutation(array_ga_input):
    array_ga = array_ga_input
    #แรนดอมวัน
    random_day_n_ga = random.randrange(0, day * 2)
    #แรนดอมในกะ
    if (pop_per_ga > 1):
        random_pop_n_ga = random.randrange(0, pop_per_ga)
    else:
        random_pop_n_ga = 0
    #แรนดอมบุคคล
    random_pop = random.randrange(0, population)
    # print("กะที่:",random_day_n_ga,"คนที่:",random_pop_n_ga,"ชื่อ:",random_pop)
    array_ga[random_day_n_ga][random_pop_n_ga] = random_pop
    return array_ga

########################################################################################################################

if(population*5 >= ((ga*pop_per_ga)*7) and population<=(pop_per_ga*6)):

    # create job in 1 week (Chromosome)
    for i in range (day*ga):
        array_pop_per_ga = []    #อาร์เรย์จำนวนคนต่อ 1 กะ
        for j in range (pop_per_ga):
            chromosome = random.randrange(0, population)
            array_pop_per_ga.append(chromosome)
        array_gaBest.append(array_pop_per_ga)
    array_ga = copy.deepcopy(array_gaBest)
    # print(array_gaBest)

    ga_more5day,gaStop_more2day,gamore_inOneDay,near_ga,moreNameInOneGa,fitnessError = findFitnessError(array_ga)
    ga_more5dayBest,gaStop_more2dayBest,gamore_inOneDayBest,near_gaBest,moreNameInOneGaBest,fitnessErrorBest = findFitnessError(array_gaBest)

    # print("\nคนที่ทำงานกะติดกัน เช่นดึกไปเช้า คือ",near_gaBest)
    # print("คนที่ทำงานเกิน 5 วัน คือ",ga_more5dayBest)
    # print("คนที่หยุดติดต่อกันเกิน 2 วัน คือ",gaStop_more2dayBest)
    # print("คนที่ทำงานมากกว่า 1 กะต่อวัน คือ",gamore_inOneDayBest)
    # print("คนที่มีชื่อเกินใน 1 กะ คือ",moreNameInOneGaBest)
    # print("ค่า fitness Error ที่ได้ คือ",fitnessErrorBest)
# mutation #############################################################################################################
    print("\n-------------Loop-------------")
    countLoop = 0
    while(fitnessErrorBest!=100):  #countLoop<10 fitnessErrorBest!=10*population-5 and
        # แบบ random
        print("Loop ที่", countLoop+1)
        for i in range(5):
            array_ga = randomMutation(array_ga)
            ga_more5day,gaStop_more2day,gamore_inOneDay,near_ga,moreNameInOneGa,fitnessError = findFitnessError(array_ga)
            if(fitnessError>=fitnessErrorBest):
                near_gaBest = copy.deepcopy(near_ga)
                ga_more5dayBest = copy.deepcopy(ga_more5day)
                gaStop_more2dayBest = copy.deepcopy(gaStop_more2day)
                gamore_inOneDayBest = copy.deepcopy(gamore_inOneDay)
                moreNameInOneGaBest = copy.deepcopy(moreNameInOneGa)
                fitnessErrorBest = fitnessError
                array_gaBest = copy.deepcopy(array_ga)
            elif(fitnessError<fitnessErrorBest):
                near_ga = copy.deepcopy(near_gaBest)
                ga_more5day = copy.deepcopy(ga_more5dayBest)
                gaStop_more2day = copy.deepcopy(gaStop_more2dayBest)
                gamore_inOneDay = copy.deepcopy(gamore_inOneDayBest)
                moreNameInOneGa = copy.deepcopy(moreNameInOneGaBest)
                fitnessError = fitnessErrorBest
                array_ga = copy.deepcopy(array_gaBest)

        # แบบเงื่อนไขให้ดีขึ้น
        if(len(moreNameInOneGa)>0 or len(gamore_inOneDay)>0 or len(near_ga)>0):
            # 1. เช็คว่าใครมีชื่อซ้ำใน 1 กะ ให้ทำการมิวเต และแรนดอมชื่ออื่น แต่ชื่อนั้นต้องไม่ซ้ำกะถัดไป (สำหรับ 1 กะมีตั้งแต่ 2 คนขึ้นไป)
            if (len(moreNameInOneGa) > 0 and pop_per_ga > 1):
                #ลบชื่อซ้ำ
                for i in range(day*2):
                    for j in range(pop_per_ga):
                        array_ga[i] = list(set(array_ga[i]))

            # 2. เช็คว่าใครทำงานกะเช้าดึก กับทำกะติดกัน ให้ทำการมิวเต และแรนดอมชื่ออื่น แต่ชื่อนั้นต้องไม่ซ้ำกะถัดไป
            if (len(gamore_inOneDay) > 0 or len(near_ga) > 0):
                # ลบชื่อซ้ำ ในกะใกล้เคียง
                for i in range(day * 2 - 1):
                    set_now = array_ga[i]
                    set_after_ga = array_ga[i + 1]
                    set_now = list(set(set_now) - set(set_after_ga))
                    array_ga[i] = set_now

            #แรนดอมชื่อ
            for i in range(day*2):
                for j in range(pop_per_ga):
                    if(len(array_ga[i])!=pop_per_ga):
                        random_remove = []
                        for k in range(population):
                            random_remove.append(k)
                        # เช็คกะเช้าวันที่ 1
                        if(i==0):
                            set_now = array_ga[i]
                            set_after_ga = array_ga[i + 1]
                            # Set กะปัจจุบัน
                            random_remove = list(set(random_remove) - set(set_now))
                            # Set กะหลัง
                            random_remove = list(set(random_remove) - set(set_after_ga))
                            # add value
                            random_name = random.randrange(0,len(random_remove))
                            array_ga[i].append(random_remove[random_name])
                        # เช็คกะเช้าวันที่ 2-6
                        elif(i<(day*2)-1):
                            set_before_ga = array_ga[i-1]
                            set_now = array_ga[i]
                            set_after_ga = array_ga[i+1]
                            # Set กะก่อนหน้า
                            random_remove = list(set(random_remove) - set(set_before_ga))
                            # Set กะปัจจุบัน
                            random_remove = list(set(random_remove) - set(set_now))
                            # Set กะหลัง
                            random_remove = list(set(random_remove) - set(set_after_ga))
                            # add value
                            random_name = random.randrange(0, len(random_remove))
                            array_ga[i].append(random_remove[random_name])
                        # เช็คกะเช้าวันที่ 7
                        else:
                            set_before_ga = array_ga[i-1]
                            set_now = array_ga[i]
                            # Set กะก่อนหน้า
                            random_remove = list(set(random_remove) - set(set_before_ga))
                            # Set กะปัจจุบัน
                            random_remove = list(set(random_remove) - set(set_now))
                            # add value
                            random_name = random.randrange(0, len(random_remove))
                            array_ga[i].append(random_remove[random_name])
                    else:
                        break

        ga_more5day, gaStop_more2day, gamore_inOneDay, near_ga, moreNameInOneGa, fitnessError = findFitnessError(array_ga)
        if (fitnessError >= fitnessErrorBest):
            near_gaBest = copy.deepcopy(near_ga)
            ga_more5dayBest = copy.deepcopy(ga_more5day)
            gaStop_more2dayBest = copy.deepcopy(gaStop_more2day)
            gamore_inOneDayBest = copy.deepcopy(gamore_inOneDay)
            moreNameInOneGaBest = copy.deepcopy(moreNameInOneGa)
            fitnessErrorBest = fitnessError
            array_gaBest = copy.deepcopy(array_ga)
        elif (fitnessError < fitnessErrorBest):
            near_ga = copy.deepcopy(near_gaBest)
            ga_more5day = copy.deepcopy(ga_more5dayBest)
            gaStop_more2day = copy.deepcopy(gaStop_more2dayBest)
            gamore_inOneDay = copy.deepcopy(gamore_inOneDayBest)
            moreNameInOneGa = copy.deepcopy(moreNameInOneGaBest)
            fitnessError = fitnessErrorBest
            array_ga = copy.deepcopy(array_gaBest)

        print("คนที่ทำงานกะติดกัน เช่นดึกไปเช้า คือ",near_gaBest)
        print("คนที่ทำงานเกิน 5 วัน คือ",ga_more5dayBest)
        print("คนที่หยุดติดต่อกันเกิน 2 วัน คือ",gaStop_more2dayBest)
        print("คนที่ทำงานมากกว่า 1 กะต่อวัน คือ",gamore_inOneDayBest)
        print("คนที่มีชื่อเกินใน 1 กะ คือ",moreNameInOneGaBest)
        print("ค่า fitness Error ที่ได้ คือ",fitnessErrorBest)
        print(array_gaBest)
        countLoop = countLoop + 1

########################################################################################################################

    print("\n-------------END-------------")
    print("คนที่ทำงานกะติดกัน เช่นดึกไปเช้า คือ",near_gaBest)
    print("คนที่ทำงานเกิน 5 วัน คือ",ga_more5dayBest)
    print("คนที่หยุดติดต่อกันเกิน 2 วัน คือ",gaStop_more2dayBest)
    print("คนที่ทำงานมากกว่า 1 กะต่อวัน คือ",gamore_inOneDayBest)
    print("คนที่มีชื่อเกินใน 1 กะ คือ",moreNameInOneGaBest)
    print("ค่า fitness Error ที่ได้ คือ",fitnessErrorBest)
    print(array_gaBest)
    print("Loop การทำงานเป็น",countLoop,"รอบ")

    # ปริ้นว่าใครทำงานวันไหนบ้าง
    print("\n------------------- Timetable -------------------")
    table_data = [['NO.', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']]
    for i in range(population):
        array_x = []
        array_x.append(i + 1)
        for j in range(day):
            sumga = 0
            for k in range(pop_per_ga):
                if (array_gaBest[j * 2][k] == i):
                    # print("เช้า", end=' ')
                    array_x.append('Day')
                    break
                elif (array_gaBest[(j * 2) + 1][k] == i):
                    # print("ดึก", end='  ')
                    array_x.append('Mid')
                    break
                else:
                    sumga = sumga + 1
                if (sumga == pop_per_ga):
                    array_x.append('-')
        table_data.append(array_x)
    table1 = AsciiTable(table_data)
    print(table1.table)
elif(population<(pop_per_ga*6)):
    print("มีจำนวนบุคลากรมากเกินไป ต้องเพิ่มจำนวนกะต่อคนเพิ่ม")
else:
    print("ไม่สามารถทำได้เนื่องจากบุคลากรไม่เพียงพอ")