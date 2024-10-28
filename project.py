#63.0 50.0 58.0
#81.0 68.0 77.0
#63.0 52.0 60.0
#82.0 70.0 79.0
#69.0 58.0 65.0

# Input
#0   61.0
#30  80.0
#60  62.0
#90  83.0
#120 68.0

# Output
#0 <= x <=        30 ; y =      61.0000 +       0.6333 x ; interpolation
#30 <= x <=       60 ; y =      98.0000 +      -0.6000 x ; interpolation
#60 <= x <=       90 ; y =      20.0000 +       0.7000 x ; interpolation
#90 <= x <=      120 ; y =     128.0000 +      -0.5000 x ; interpolation

# Begin quoted code from Thomas Kennedy at
# https://odumedia.mediaspace.kaltura.com/media/2024+CS417+-+Semester+Project+Getting+Started+-+Interpolation/1_au89jcla

#def interpolate_line(times: list[float], readings: list[float]) -> None:
    # Compute slope
    #m = (y_1 - y_0) / (x_1 - x_0)
    #slope = (readings[1] - readings[0]) / (times[1] - times[0])

#    for k in range(len(times)):
#        slope = (readings[k + 1] - readings[k]) / (times[k + 1] - times[k])
    
    # Compute y-intercept
#        y_intercept = readings[k] - (slope * times[k])

#        print(f"{slope=} {y_intercept=}")

# End quoted code

def interpolate_line(times, readings):
    # added -1 to length because it was giving me an error message that it was out of bounds before doing so

    for i in range(len(times) - 1):
        slope = (readings[i + 1] - readings[i]) / (times[i + 1] - times[i])
        y_intercept = readings[i] - (slope * times[i])
        print(f" {times[i]} <= x <= {times[i+1]} ; {y_intercept} + {slope} x ; interpolation")

if __name__ == '__main__':
    times = [0, 30, 60 , 90, 120]
    readings_core_0 = [61.0, 80.0, 62.0, 83.0, 68.0]
    readings_core_1 = [63.0, 81.0, 63.0, 82.0, 69.0]
    readings_core_2 = [50.0, 68.0, 52.0, 70.0, 58.0]
    readings_core_3 = [58.0, 77.0, 60.0, 79.0, 65.0]
    
    interpolate_line(times, readings_core_0)
    print()
    interpolate_line(times, readings_core_1)
    print()
    interpolate_line(times, readings_core_2)
    print()
    interpolate_line(times, readings_core_3)
