fn main() {
    
    let response = reqwest::blocking::get(
        "https://crypto.com/price",
    )
    .unwrap()
    .text()
    .unwrap();

    let mut wtr=csv::Writer::from_path("crypto.csv").unwrap();
    wtr.write_record(&["Crypto Name","Price","24H Change","24H Volume","Market Cap"]).unwrap();

    let document = scraper::Html::parse_document(&response);

    let crypto_selector=scraper::Selector::parse("tr.css-1cxc880").unwrap();
    let crypto_name_selector=scraper::Selector::parse("span.chakra-text.css-1jj7b1a").unwrap();
    let crypto_price_selector=scraper::Selector::parse("div.css-b1ilzc").unwrap();
    let crypto_24hchange_selector=scraper::Selector::parse("td.css-1b7j986 p").unwrap();    

    let crypto_24hvolume_selector=scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let crypto_marketcap_selector=scraper::Selector::parse("td.css-1nh9lk8+td").unwrap();

    for element in document.select(&crypto_selector){
        let crypto_name_element=element.select(&crypto_name_selector).next().expect("crypto name");
        let crypto_name=crypto_name_element.text().collect::<String>();

        let crypto_price_element = element.select(&crypto_price_selector).next().expect("Could not select crypto price");
        let crypto_price = crypto_price_element.text().collect::<String>();
  
        let crypto_24hchange_element = element.select(&crypto_24hchange_selector).next().expect("Could not select 24hchange");
        let crypto_24hchange = crypto_24hchange_element.text().collect::<String>();

        let crypto_24hvolume_element = element.select(&crypto_24hvolume_selector).next().expect("Could not select 24hvolume");
        let crypto_24hvolume = crypto_24hvolume_element.text().collect::<String>();


        let crypto_marketcap_element = element.select(&crypto_marketcap_selector).next().unwrap();
        let crypto_marketcap = crypto_marketcap_element.text().collect::<String>();
        println!("done");

        wtr.write_record([&crypto_name,&crypto_price,&crypto_24hchange,&crypto_24hvolume,&crypto_marketcap]).expect("Could not create selector.");
    wtr.flush().expect("could not close file");
    } 
}
