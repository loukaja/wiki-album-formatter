"""Main module to be run
"""

import time

from helpers import fill_album_info_box, fill_tracklist, fill_lineup, get_reviews, add_reviews, add_external_links


def run(link, reviews, members, external_links):
    """Main function to be run

    Args:
        link (string): Tidal album link, for example: 'https://tidal.com/browse/album/102314585'
    """

    # Grab the ID from the album link
    url_id = link.split('/')[-1]

    file_and_album = fill_album_info_box(url_id)

    # Sleep for a second so we don't hammer the API too often
    time.sleep(1)

    fill_tracklist(url_id, file_and_album)

    print(f"Members: {members}")

    print("Filling in member data")
    fill_lineup(file_and_album, members)

    if reviews:
        print("Getting review data")
        review_list = get_reviews(reviews)

        add_reviews(review_list, file_and_album)

    print(external_links)
    # add_external_links(external_links)
