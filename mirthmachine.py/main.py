import requests

def generate_meme(username, password, template_id, text0, text1):
    url = "https://api.imgflip.com/caption_image"
    params = {
        "template_id": template_id,
        "username": username,
        "password": password,
        "text0": text0,
        "text1": text1
    }
    response = requests.post(url, params=params)
    data = response.json()
    if data["success"]:
        meme_url = data["data"]["url"]
        return meme_url
    else:
        error_message = data["error_message"]
        raise ValueError(f"Error generating meme: {error_message}")


def get_memes():
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)
    data = response.json()
    memes = data["data"]["memes"]
    return memes


def main():
    # Enter your ImgFlip credentials here
    username = "osama123"
    password = "osama098"

    keyword = input("Enter a keyword: ")

    # Get the list of memes
    memes = get_memes()

    # Filter memes based on the keyword
    filtered_memes = [meme for meme in memes if keyword.lower() in meme["name"].lower()]

    if len(filtered_memes) == 0:
        print("No memes found for the keyword.")
        return

    # Select a random meme
    print("Memes related to the keyword:")
    for i, meme in enumerate(filtered_memes, start=1):
        print(f"{i}. {meme['name']}")

        choice = int(input("Enter the number of the meme you want to generate: "))

    if choice < 1 or choice > len(filtered_memes):
        print("Invalid choice.")
        return

    # Select the chosen meme
    selected_meme = filtered_memes[choice - 1]
    template_id = selected_meme["id"]

    top_text = input("Enter the text for the top caption: ")
    bottom_text = input("Enter the text for the bottom caption: ")

    try:
        meme_url = generate_meme(username, password, template_id, top_text, bottom_text)
        print("Meme generated successfully!")
        print("Meme URL:", meme_url)

        # Download the meme image
        response = requests.get(meme_url)
        with open("meme.jpg", "wb") as f:
            f.write(response.content)
        print("Meme image downloaded successfully!")
    except ValueError as e:
        print("Error generating meme:", str(e))


if __name__ == "__main__":
    main()        


