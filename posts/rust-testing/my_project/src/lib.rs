// src/lib.rs

/// Adds two numbers together.
///
/// # Examples
///
/// ```
/// let result = my_project::add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

pub struct Rectangle {
    pub width: u32,
    pub height: u32,
}

impl Rectangle {
    /// Returns the area of the rectangle.
    ///
    /// # Examples
    ///
    /// ```
    /// let rect = my_project::Rectangle { width: 3, height: 4 };
    /// assert_eq!(rect.area(), 12);
    /// ```
    pub fn area(&self) -> u32 {
        self.width * self.height
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn test_area() {
        let rect = Rectangle { width: 3, height: 4 };
        assert_eq!(rect.area(), 12);
    }

    #[test]
    #[should_panic]
    fn test_add_panic() {
        panic!("This test should panic!");
    }
}

