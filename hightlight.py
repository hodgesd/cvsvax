import fitz
import re
import PyPDF2 as PDF



### Search and Hightlight 1 Phase

# ### READ IN PDF
doc = fitz.open("PHNL.pdf")

# for page in doc:
#     ### SEARCH
#     text = "CLOSED"
#     text_instances = page.searchFor(text)
#
#     ### HIGHLIGHT
#     for inst in text_instances:
#         highlight = page.addHighlightAnnot(inst)
#         highlight.update()

### Search and hightlight multiple phrases

# terms = ["CLOSED", "U/S"]
terms = ["CLOSED", "U/S", "PPR", "UNUSABLE", "CLSD", "TFR", "NA", "TEMPORARY FLIGHT RESTRICTIONS"]


for text in terms:
    for page in doc:
        ### SEARCH
        # text = "CLOSED"
        # text = ["CLOSED", "U/S", "PPR", "UNUSABLE", "CLSD", "TFR", "NA", "TEMPORARY FLIGHT RESTRICTIONS"]

        text_instances = page.searchFor(text)

        ### HIGHLIGHT
        for inst in text_instances:
            highlight = page.addHighlightAnnot(inst)
            # highlight.setColors({"stroke":(0, 0, 1), "fill":(1.0, 0.0, 0.0)})
            highlight.setColors(stroke=(255.0/255.0, 0.0/255.0, 0.0/255.0))
            highlight.update()



### OUTPUT
doc.save("output.pdf", garbage=4, deflate=True, clean=True)
