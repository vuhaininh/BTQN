export const dateFormat = (date, format) => {
  const inputDay = new Date(date);
  let dd = inputDay.getDate();

  let mm = inputDay.getMonth() + 1;
  let yyyy = inputDay.getFullYear();
  if (dd < 10) {
    dd = `0${dd}`;
  }

  if (mm < 10) {
    mm = `0${mm}`;
  }
  if (format === 'dd/mm/yyyy') return `${dd}/${mm}/${yyyy}`;
};

export const getLiabilityColor = (liability, liabilityLimit) => {
  const percent = (liability * 100) / liabilityLimit;
  let color = '';
  if (percent <= 60) color = 'success';
  else if (percent <= 80) color = 'warning';
  else color = 'error';
  return color;
};
