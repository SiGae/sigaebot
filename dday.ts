export = async (rawQuery: string) => {
  let yyyy: number = -1;
  let mm: number = -1;
  let dd: number = -1;
  const convertQuery: string = rawQuery.substring(6);
  console.log(convertQuery);
  if (convertQuery.split(",").length === 3) {
    yyyy = parseInt(convertQuery.split(",")[0]);
    mm = parseInt(convertQuery.split(",")[1]) - 1;
    dd = parseInt(convertQuery.split(",")[2]);
  } else if (convertQuery.split(".").length === 3) {
    yyyy = parseInt(convertQuery.split(".")[0]);
    mm = parseInt(convertQuery.split(".")[1]) - 1;
    dd = parseInt(convertQuery.split(".")[2]);
  } else if (convertQuery.split("-").length === 3) {
    yyyy = parseInt(convertQuery.split("-")[0]);
    mm = parseInt(convertQuery.split("-")[1]) - 1;
    dd = parseInt(convertQuery.split("-")[2]);
  } else if (convertQuery.split(" ").length === 3) {
    yyyy = parseInt(convertQuery.split(" ")[0]);
    mm = parseInt(convertQuery.split(" ")[1]) - 1;
    dd = parseInt(convertQuery.split(" ")[2]);
  } else {
    return "Error!";
  }

  // Input date
  const inputDate = new Date(yyyy, mm, dd);
  // Current date
  const nowDate = new Date();
  // Time diff
  const timeDiff = inputDate.getTime() - nowDate.getTime();
  // Day diff
  const diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));

  let output = "";

  if (diffDays === 0) {
    output = "오늘이에요!";
  } else if (diffDays < 0) {
    output = Math.abs(diffDays) + "일 지났어요!";
  } else if (diffDays > 0) {
    output = diffDays + "일 남았어요!";
  }

  return output;
};
