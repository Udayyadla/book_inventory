export function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}
export function validatePassword(password) {
  const regex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  return regex.test(password);
}

export function validateName(name) {
  const regex =
    /^(?!.*(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz))[A-Za-z\s]{4,}$/i;
  return regex.test(name);
}
export function validateDate(date) {
  let today = new Date();
  let selectedDate = new Date(date);

  return selectedDate < today
    
}
export function validatebook(name) {
  const regex =
    /^(?!.*(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz))[A-Za-z\s]{2,}$/i;
  return regex.test(name);
}

export function validateAutorName(name) {
  const regex =
    /^(?!.*(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz))[A-Za-z\s]{2,}$/i;
  return regex.test(name);
}
export function validatePrice(price) { 
   
    return price>0
}