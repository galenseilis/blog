use gcd::Gcd;

fn main() {
    let x: u64 = 2024;
    let y: u64 = 748;
    println!("gcd({}, {}) = {}", x, y, x.gcd(y));
}
