import os

def read_slides_dir():
    """

    """
    if not os.path.exists('slides'):
        # exception?
        pass

    files = os.listdir('slides')

    files_list = []

    for slide in files:
        if slide.endswith('.md'):
            files_list.append(slide)

    return files_list


