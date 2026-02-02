-- Create or replace the user_metrics_view__staging view
CREATE OR REPLACE VIEW user_metrics_view__staging AS
SELECT
 user_id,
 -- Calculate total revenue for purchase events
 SUM(CASE WHEN event_type = 'purchase' THEN revenue ELSE 0 END) AS total_revenue,
 -- Count all events
 COUNT(*) AS total_events,
 -- Calculate average revenue per event, handling division by zero
 CASE WHEN COUNT(*) = 0 THEN 0 ELSE SUM(CASE WHEN event_type = 'purchase' THEN revenue ELSE 0 END) / COUNT(*) END AS avg_revenue_per_event
FROM raw_events
GROUP BY user_id;