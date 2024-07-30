-- 코드를 입력하세
with p as (
SELECT * from patient
join appointment using(PT_NO)
where date_format(APNT_YMD, "%Y-%m-%d") = "2022-04-13" and APNT_CNCL_YN = "N" and MCDP_CD = "CS")

select p.APNT_NO, p.PT_NAME, p.PT_NO, doctor.MCDP_CD, doctor.dr_name, p.apnt_ymd from p
join doctor on p.MDDR_ID = doctor.DR_ID
order by p.apnt_ymd