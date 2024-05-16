#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def github() -> str:
    """
    Returns a link to this file in my github repository.
    """

    return "https://github.com/jkirsch8/econ481/blob/main/HW6.py"


# In[1]:


def std() -> str:
    """
    Returns a SQL query for the auctions database 
    and returns standard deviation of bids by item.
    """
    q = """
    SELECT itemId,
    SQRT(SUM((bidamount-avg_bid) * (bidamount-avg_bid)) / (COUNT(bidamount) - 1)) as std
    FROM 
        (SELECT itemId,
        bidamount,
        AVG(bidamount) OVER (PARTITION BY itemId) as avg_bid
        FROM bids)
    GROUP BY itemId
    HAVING count(bidamount) >1
    """
    return q


# In[3]:


print(std())


# In[ ]:


def bidder_spend_frac() -> str:
    """
    Returns a SQL query to extract total spend and total bids for each bidder.
    """
    q = """
    SELECT b.bidderName
    , b.total_bids as total_bids
    , s.total_spend as total_spend
    , s.total_spend / b.total_bids as spend_frac
    FROM
        (SELECT bidderName
        , SUM(maxbid) as total_bids
        FROM (
            SELECT bidderName
            , itemId
            , MAX(bidamount) as maxbid
            FROM bids
            GROUP BY bidderName, itemId
            )
        GROUP BY bidderName) as b
    LEFT JOIN
        (SELECT bidderName
        , SUM(maxbid) as total_spend
        FROM(
            SELECT bidderName
            , MAX(bidamount) as maxbid
            FROM bids
            GROUP BY itemID
        )
        GROUP BY bidderName) as s
    ON b.bidderName = s.bidderName
    
    """
    return q


# In[ ]:


def min_increment_freq() -> str:
    """
    Returns a SQL query that outputs a table containing the frequency of bids
    that are exactly the minimum bid increment above the previous bid.
    """
    q = """
    SELECT avg(isminbid) as freq
    FROM (
        SELECT i.bidIncrement
        , b.itemId, b.bidAmount,
        (b.bidamount - lag(bidamount) over (partition by b.itemId order by bidtime))  as increment
        , i.bidIncrement == (b.bidamount - lag(bidamount) over (partition by b.itemId order by bidtime)) as isminbid
        FROM bids as b
        INNER JOIN items as i
        ON i.itemId = b.itemId
        WHERE i.isbuynowused = 0)
    WHERE increment IS NOT NULL
    """
    return q


# In[ ]:


def win_perc_by_timestamp() -> str:
    """
    Returns a SQL Query to output a table with timestamp bin and win percentage.
    """
    q = """
    SELECT time_norm as timestamp_bin,
    AVG(iswinbid) as win_perc
    
    FROM
        (select b.itemid, b.bidtime,
        CAST(((julianday(endtime)-julianday(bidtime)) / a.length)*10 as INTEGER) + 1 as time_norm,
        b.bidamount == max(bidamount) over (partition by b.itemid) as iswinbid
        from bids as b
        inner join (
            select itemid, starttime, endtime, 
            julianday(endtime) - julianday(starttime) as length
            from items
        ) as a
        on b.itemid=a.itemid
        )
    GROUP BY timestamp_bin
    """
    return q

