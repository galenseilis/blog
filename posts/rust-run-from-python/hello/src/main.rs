fn main() {
    
    let mut count = 0;

    loop {
        count = count + 1;
        println!("{} Hello, world!", count);
        if count > 11 {
            break
        }
    }
}
