use my_project::{add, Rectangle};

#[test]
fn test_integration_add() {
    assert_eq!(add(10, 20), 30);
}

#[test]
fn test_integration_area() {
    let rect = Rectangle { width: 5, height: 6};
    assert_eq!(rect.area(), 30);
}
