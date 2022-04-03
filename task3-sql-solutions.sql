-- 1) Cities frequently Visited ?

select v.city_id_visited, c.city_name, count(v.city_id_visited) from visits v join city  c
on v.city_id_visited = c.city_id
group by city_id_visited, city_name
having count(v.city_id_visited) > 1


-- 2) Customers visited more than 1 city

select customer_id, count(city_id_visited) from visits
group by customer_id
having count(city_id_visited) > 1

-- 3) Cities Visited  break down by gender
select v.city_id_visited, cus.gender, c.city_name,cus.customer_name from visits v
join customer cus
on v.customer_id = cus.customer_id
join city c
on v.city_id_visited = c.city_id


-- 4) List the city names that are not visited by every customer and order them by the expense budget in ascending order?

select a.city_id, a.city_name,a.customer_id from
(select * from city,customer ) a
left join
visits v
on v.customer_id = a.customer_id
and v.city_id_visited = a.city_id
where v.customer_id IS NULL
order by customer_id;

-- 5) Visit/travel Percentage for every customer?

select customer_id , (count(*)::FLOAT / (select count(*) from city) ) * 100  from visits
group by customer_id;

-- 6) Total expense incurred by customers on their visits?

select v.customer_id,sum(c.expense) from visits v
join
city c
on c.city_id = v.city_id_visited
group by v.customer_id

-- 7) list the Customer details along with the city they first visited and the date of visit?


with cust_fisrt_visit  AS (
select v.customer_id , c.customer_name, v.date_visited,
dense_rank() over (partition by v.customer_id order by v.date_visited) as rank_
from visits v
join customer c
on v.customer_id = c.customer_id
)
select customer_id , customer_name, date_visited from cust_fisrt_visit
where rank_ = 1;
