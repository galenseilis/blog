fn gcd(mut n: u64, mut m: u64) -> u64 {
    assert!(n != 0 && m != 0);
    while m != 0 {
        if m < n {
            let t = m;
            m = n;
            n = t;
        }
        m = m % n;
    }
    n
}

fn main() {
    let x: u64 = 2024;
    let y: u64 = 748;
    println!("gcd({}, {}) = {}", x, y, gcd(x, y));
}
