import us_news


def scrape_health_care_rankings():
    rankings = us_news.get_rankings("health-care")

    for ranking in rankings:
        print(ranking["state"], ranking["rank"])


if __name__ == "__main__":
    scrape_health_care_rankings()
