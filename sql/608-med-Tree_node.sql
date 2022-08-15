# 608. Tree Node - medium - 2021:Amzn/Uber
# Objective: Write/convert a TreeNode object's node identification table
# observations: 1) root nodes won't have a p_id.
# 2) leaf-only nodes will not have children, so their ids would't be mentioned
#in any other p_id.
# 3) leaf-parent ('inner') nodes would/must be mentioned by others as p_id's

# Union solution:
SELECT id, 'Root' as type FROM Tree
    WHERE p_id IS NULL
UNION 
SELECT id, 'Leaf' as type FROM Tree
    WHERE id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL)
    AND p_id IS NOT NULL
UNION
SELECT id, 'Inner' as type FROM TREE
    WHERE id IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL)
    AND p_id IS NOT NULL ;
    


# second way, using CASE:
SELECT
    id AS `Id`,
    CASE # can also do IF ELSE
        WHEN tree.id = (SELECT atree.id FROM tree AS atree WHERE atree.p_id IS NULL)
          THEN 'Root'
        WHEN tree.id IN (SELECT atree.p_id FROM tree AS atree)
          THEN 'Inner'
        ELSE 'Leaf'
    END AS Type
FROM
    tree
ORDER BY `Id`;



# third way: by using IF(this cond is True then A otherwise B, A, B)
SELECT
    atree.id,
    IF(ISNULL(atree.p_id),
        'Root',
        IF(atree.id IN (SELECT p_id FROM tree), 'Inner','Leaf')) AS Type
FROM
    tree AS atree
ORDER BY atree.id
