import time
try:
    secs_since_1970 = time.time()
    formatted_secs = f"{secs_since_1970:,.4f}"
    scientific_notation = "{:.2e}".format(secs_since_1970)

    print("Seconds since January 1, 1970:", formatted_secs, "or",
          scientific_notation, "in scientific notation")
    print(time.strftime("%b %d %Y", time.localtime(secs_since_1970)))

except Exception as e:
    print("An error occured " + str(e))
