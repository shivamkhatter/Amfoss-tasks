fn main() {
    
    let response = reqwest::blocking::get(
        "https://crypto.com/price",
    )
    .unwrap()
    .text()
    .unwrap();

    let document = scraper::Html::parse_document(&response);

    let title_selector = scraper::Selector::parse ("p.chakra-text.css-rkws3 , div.css-b1ilzc , p.chakra-text.css-dg4gux , td.css-1nh9lk8").unwrap();

    let titles = document.select(&title_selector).map(|x| x.inner_html());

    titles
        .zip(1..215)
        .for_each(|(item, number)| println!("{}. {}", number, item  ));
}