"""
Default Parameter Values
"""

# The following function is designed to format text.
# This acts by centering text between Asterisks for printing out compact messages.

def banner_text(text=" ", screen_width=60):   # specifies default parameter value for text & screen_width, but can be overwritten with specified argument
    if len(text) > screen_width - 6:
        raise ValueError("String {0} is larger than the specified with {1}"
                         .format(text, screen_width))

    if text == "#":
        print("#" * screen_width) 
    else:
        output_string = "## {0} ##".format(text.center(screen_width - 6))    # can use ljust() or rjust() to align left/right rather than center 
        print(output_string) 
        
        
# Example Banners 
banner_text("#")
banner_text(" ")
banner_text("Analyst: Dan Collins")
banner_text("Date: 02/02/2020")
banner_text(" ")
banner_text("#") 

# changing the default screen_width 
banner_text("Hello", 30)   # you can see, this output looks different as we changed the default value 
