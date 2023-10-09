def get_vlm_prompt():
    return '''you are very good at deeply analyzing the contents of an image and based on what you see, you output a highly valuable and informative summary. The summary covers all of the information and content shown in the image.
Hence your goal is to Deeply analyse this image and based on what you see, output a step by step walkthrough of all the events happening in the image. 
For example:-
1. If the image shows a chat screenshot between two people, you deeply analyze each text and answer the question "what is being discussed in this image?".
2. If the image is of a food item, you carefully identify the food item along with specific details like the ingredients, seasoning, topping, sauces etc. and based on these identifications, give a clear description of the food item.
3. If the image shows a clothing apparel, you carefully identify the apparel along with specific details like the color, style, detailing etc. and based on these identifications, give a clear description of the clothing apparel.

Summary:'''

def get_llm_prompt():
    return '''hey, consider yourself as being very good at reading image descriptions, and converting them to certain instructions that humans can follow to accomplish a task. 
The image descriptions are generated using a vision language model and the images were usually of products like food dishes, clothes, furniture etc. or chat conversations between people about meetings, flight bookings etc. your job is to infer all the details about the main thing that is being talked about in the image descriptions and provide fully informative human understandable instructions based on your analysis of the image descriptions. the instructions should contain full details so that they are complete for a human to follow.
Following examples depict how your behaviour should be like -
For example,
1. image description: The image shows a pizza with various toppings, including vegetables, cheese, and meat. The pizza is placed on a wooden table, which provides a rustic and natural setting for the dish. The image is a close-up shot of the pizza, allowing for a detailed examination of the various ingredients and toppings.
Your instruction: order a pizza with various toppings, including vegetables, cheese, and meat from doordash.

2. image description: The image shows a pink one-piece swimsuit, which is a type of clothing apparel. The swimsuit is designed for young girls and is made of a soft, stretchy material that allows for a comfortable fit and ease of movement. The swimsuit is a one-piece design, which means it covers the entire body, including the arms and legs, providing a complete coverage for the wearer.
Your instruction: order a pink one-piece swimsuit made of a soft, stretchy material from amazon.

3. image description: the image shows a chat screenshot between two people who are discussing a meeting time fir for both of them. first user proposed 6pm tuesday as a suitable time to which the second user agreed, and asked if herumbshandilya123@gmail.com is the correct email address for the first user to which the first user said yes.
Your instruction: schedule a meeting for 6pm this tuesday at the address herumbshandilya123@gmail.com.

Remember you should focus on the main thing that is being talk about in the image description and include all of the details about that  main thing as shown in the examples above. also notice how the instructions in the above examples are easy to follow as they include the name of the website as well. 
Now based on these examples, generate proper instruction for the following textual image description:  
'''